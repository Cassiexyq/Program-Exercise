#include<iostream>
#include<stdio.h>
using namespace std;

struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
        val(x), next(NULL) {
    }
};
class Solution {
public:
    ListNode* EntryNodeOfLoop(ListNode* pHead)
    {
    	if (!pHead || !pHead->next)  return NULL;
    	
    	ListNode *slow = pHead;
    	ListNode *fast = pHead;
    	while (fast && fast->next){
    		fast = fast->next->next;
    		slow = slow->next;
    		if (slow == fast){
    			break;
    		}
    	}
    	if (slow == fast){
    		fast = pHead;
    		while(slow != fast){
    			slow = slow->next;
    			fast = fast->next;
    		}
    		return slow;
    	}
		
		return NULL;
    }
};