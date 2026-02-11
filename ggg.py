import requests
import json
import os
import re
import time
from datetime import datetime


class LeetCodeTop150Scraper:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://leetcode.com/graphql"
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Origin": "https://leetcode.com",
            "Referer": "https://leetcode.com/studyplan/top-interview-150/"
        }
        self.base_output_dir = "leetcode_top_150_pre2023"
        os.makedirs(self.base_output_dir, exist_ok=True)

        # Ustawienie daty granicznej: 1 Maja 2023
        self.cutoff_date = datetime(2023, 5, 1)

    def get_top_150_list(self):
        """Pobiera listę zadań z planu Top Interview 150"""
        print("Pobieranie listy zadań Top 150...")
        query = """
        query studyPlanV2Detail($planSlug: String!) {
          studyPlanV2Detail(planSlug: $planSlug) {
            planSubGroups {
              slug
              questions {
                title
                titleSlug
                questionFrontendId
                difficulty
              }
            }
          }
        }
        """
        variables = {"planSlug": "top-interview-150"}

        try:
            resp = self.session.post(self.base_url, json={"query": query, "variables": variables}, headers=self.headers)
            data = resp.json()

            questions = []
            groups = data['data']['studyPlanV2Detail']['planSubGroups']
            for group in groups:
                questions.extend(group['questions'])

            print(f"Znaleziono {len(questions)} zadań.")
            return questions
        except Exception as e:
            print(f"Błąd podczas pobierania listy zadań: {e}")
            return []

    def extract_python_code(self, content):
        """Wyciąga kod Pythona z Markdowna"""
        content = content.replace('\\n', '\n').replace('\\t', '\t')
        match = re.search(r'```(?:python3?|py)(.*?)\n(.*?)```', content, re.DOTALL | re.IGNORECASE)

        if match:
            code = match.group(2).strip()
            code = code.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&quot;', '"')
            return code

        match_generic = re.search(r'```\n(.*?)```', content, re.DOTALL)
        if match_generic:
            code = match_generic.group(1).strip()
            return code

        return None

    def save_solution(self, directory, filename, content):
        path = os.path.join(directory, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    def run_for_problem(self, question, target_count=10):
        title_slug = question['titleSlug']
        problem_id = question['questionFrontendId']

        folder_name = f"{problem_id.zfill(4)}-{title_slug}"
        task_dir = os.path.join(self.base_output_dir, folder_name)
        os.makedirs(task_dir, exist_ok=True)

        print(f"[{problem_id}] {question['title']} -> Szukam rozwiązań przed {self.cutoff_date.date()}...")

        self.headers["Referer"] = f"https://leetcode.com/problems/{title_slug}/solutions/"

        query = """
        query communitySolutions($questionSlug: String!, $skip: Int!, $first: Int!, $query: String, $orderBy: TopicSortingOption, $languageTags: [String!], $topicTags: [String!]) {
          questionSolutions(
            filters: {questionSlug: $questionSlug, skip: $skip, first: $first, query: $query, orderBy: $orderBy, languageTags: $languageTags, topicTags: $topicTags}
          ) {
            solutions {
              id
              title
              post {
                creationDate
                voteCount
                content
              }
            }
          }
        }
        """

        # Fetch buffer: Pobieramy 40, żeby mieć z czego wybierać po odrzuceniu nowych
        variables = {
            "questionSlug": title_slug,
            "skip": 0,
            "first": 40,
            "query": "",
            "orderBy": "most_votes",
            "languageTags": ["python", "python3"],
            "topicTags": []
        }

        try:
            r = self.session.post(self.base_url, json={"query": query, "variables": variables}, headers=self.headers)
            if r.status_code != 200:
                print(f"  Blad HTTP: {r.status_code}")
                return

            data = r.json()
            if 'errors' in data:
                print(f"  Blad GraphQL: {data['errors'][0]['message']}")
                return

            solutions = data['data']['questionSolutions']['solutions']
            saved_count = 0

            for sol in solutions:
                if saved_count >= target_count:
                    break

                ts = sol['post']['creationDate']
                creation_dt = datetime.fromtimestamp(ts)

                # --- FILTRACJA DATY ---
                if creation_dt >= self.cutoff_date:
                    # Pomijamy to rozwiązanie, jest za nowe
                    continue
                # ----------------------

                raw_content = sol['post']['content']
                clean_code = self.extract_python_code(raw_content)

                if clean_code:
                    votes = sol['post']['voteCount']
                    date_str = creation_dt.strftime('%Y-%m-%d')
                    sol_id = sol['id']

                    filename = f"votes{votes}_{date_str}_{sol_id}.py"
                    self.save_solution(task_dir, filename, clean_code)
                    saved_count += 1

            print(f"  Zakończono. Zapisano {saved_count}/{target_count} rozwiązań (pre-2023-05).")

        except Exception as e:
            print(f"  Błąd przetwarzania zadania {title_slug}: {e}")

    def scrape_all(self, target_count_per_problem=10):
        questions = self.get_top_150_list()

        for idx, q in enumerate(questions):
            self.run_for_problem(q, target_count=target_count_per_problem)

            time.sleep(1.5)

            if (idx + 1) % 10 == 0:
                print(f"--- Przetworzono {idx + 1}/150 zadań ---")


if __name__ == "__main__":
    scraper = LeetCodeTop150Scraper()
    scraper.scrape_all(target_count_per_problem=10)