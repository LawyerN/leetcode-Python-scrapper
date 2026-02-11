class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if(head==NULL){
            return NULL;
        }
        ListNode* ptr=head;
        vector<int> vec;
        while(ptr){
            vec.push_back(ptr->val);
            ptr=ptr->next;
        }
        sort(vec.begin(),vec.end());
        ListNode* n = new ListNode(vec[0]);
        head=n;
        ListNode* temp=head;
        for(int i=1;i<vec.size();i++){
            ListNode* n1 = new ListNode(vec[i]);
            temp->next=n1;
            temp=temp->next;
            
        }
        return head;
    }
};