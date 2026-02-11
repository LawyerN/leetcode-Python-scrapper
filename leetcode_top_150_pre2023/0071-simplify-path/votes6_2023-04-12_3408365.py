class Solution:
    def simplifyPath(self, path: str) -> str:
        return __import__(\'os\').path.abspath(path)