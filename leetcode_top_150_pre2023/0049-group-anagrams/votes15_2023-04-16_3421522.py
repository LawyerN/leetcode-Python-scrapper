class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        vector<vector<string>> ans;

        map<map<char,int>, vector<string>> mp;
        int n = strs.size();
        string temp;
        
        for(int i=0;i<n;i++)
        {
            map<char,int> temp;
            for(char c:strs[i]){
                temp[c]++;
            }

            mp[temp].push_back(strs[i]);
        }


        for(auto itr=mp.begin();itr!=mp.end();itr++)
        {
            ans.push_back(itr->second);
        }

        return ans;


        
    }
};