import requests
import json
import os
import re
from datetime import datetime

class LeetCodePythonScraper:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://leetcode.com/graphql"
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Origin": "https://leetcode.com"
        }
        self.output_dir = "human_generated_solutions"
        os.makedirs(self.output_dir, exist_ok=True)

    def get_problem_details(self, title_slug):
        query = """
        query questionTitle($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            questionFrontendId
            titleSlug
          }
        }
        """
        try:
            resp = self.session.post(self.base_url, json={"query": query, "variables": {"titleSlug": title_slug}}, headers=self.headers)
            data = resp.json()
            return data['data']['question']['questionFrontendId']
        except:
            return "0000"

    def extract_python_code(self, content):
        content = content.replace('\\n', '\n').replace('\\t', '\t')
        match = re.search(r'```python3?.*?\n(.*?)```', content, re.DOTALL | re.IGNORECASE)
        
        if match:
            code = match.group(1).strip()
            code = code.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
            return code
        return None

    def save_solution(self, filename, content):
        path = os.path.join(self.output_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Zapisano: {path}")

    def run(self, task_name, target_count=10):
        slug = task_name.lower().replace(" ", "-")
        self.headers["Referer"] = f"[https://leetcode.com/problems/](https://leetcode.com/problems/){slug}/solutions/"
        
        problem_id = self.get_problem_details(slug)
        problem_id_str = problem_id.zfill(4) 
        
        print(f"Zadanie: [{problem_id}] {task_name}")

        query_meta = """
        query communitySolutions($questionSlug: String!, $skip: Int!, $first: Int!, $query: String, $orderBy: TopicSortingOption, $languageTags: [String!], $topicTags: [String!]) {
          questionSolutions(
            filters: {questionSlug: $questionSlug, skip: $skip, first: $first, query: $query, orderBy: $orderBy, languageTags: $languageTags, topicTags: $topicTags}
          ) {
            totalNum
          }
        }
        """
        
        variables_meta = {
            "questionSlug": slug,
            "skip": 0,
            "first": 1,
            "query": "",
            "orderBy": "newest_to_oldest",
            "languageTags": [], # Puste! To klucz do działania
            "topicTags": []
        }

        try:
            r = self.session.post(self.base_url, json={"query": query_meta, "variables": variables_meta}, headers=self.headers)
            if r.status_code != 200:
                print(f"Blad HTTP: {r.status_code}")
                return
            data = r.json()
            if 'errors' in data:
                print(f"Blad GraphQL: {data['errors'][0]['message']}")
                return
                
            total = data['data']['questionSolutions']['totalNum']
            print(f"Lacznie rozwiazan (wszystkie jezyki): {total}")
        except Exception as e:
            print(f"Blad pobierania metadanych: {e}")
            return

        fetch_buffer = 150
        skip = max(0, total - fetch_buffer)
        
        print(f"Pobieranie {fetch_buffer} najstarszych postow do analizy...")
        
        query_list = """
        query communitySolutions($questionSlug: String!, $skip: Int!, $first: Int!, $query: String, $orderBy: TopicSortingOption, $languageTags: [String!], $topicTags: [String!]) {
          questionSolutions(
            filters: {questionSlug: $questionSlug, skip: $skip, first: $first, query: $query, orderBy: $orderBy, languageTags: $languageTags, topicTags: $topicTags}
          ) {
            solutions {
              id
              title
              post {
                creationDate
                content
              }
            }
          }
        }
        """
        
        variables_list = {
            "questionSlug": slug,
            "skip": skip,
            "first": fetch_buffer,
            "query": "",
            "orderBy": "newest_to_oldest",
            "languageTags": [], # Puste! Filtrujemy lokalnie
            "topicTags": []
        }
        
        try:
            r = self.session.post(self.base_url, json={"query": query_list, "variables": variables_list}, headers=self.headers)
            solutions = r.json()['data']['questionSolutions']['solutions']
            
            solutions.sort(key=lambda x: x['post']['creationDate'])

            saved_count = 0
            date_counters = {} 

            for sol in solutions:
                if saved_count >= target_count:
                    break

                raw_content = sol['post']['content']
                
                clean_code = self.extract_python_code(raw_content)

                if clean_code:
                    ts = sol['post']['creationDate']
                    date_str = datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    
                    base_name = f"{problem_id_str}-{slug}_{date_str}"
                    
                    if base_name in date_counters:
                        date_counters[base_name] += 1
                        filename = f"{base_name}_{date_counters[base_name]}.txt"
                    else:
                        date_counters[base_name] = 0
                        filename = f"{base_name}.txt"
                    
                    self.save_solution(filename, clean_code)
                    saved_count += 1
            
            print(f"Zakonczono. Zapisano {saved_count}/{target_count} plikow.")
            if saved_count < target_count:
                print("Wskazowka: Jesli plikow jest za malo, zwieksz 'fetch_buffer' w kodzie.")

        except Exception as e:
            print(f"Blad: {e}")

if __name__ == "__main__":
    scraper = LeetCodePythonScraper()
    scraper.run("Two Sum", target_count=10)