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
    ListNode EntryNodeOfLoop(ListNode pHead)
    {
    	if(pHead == NULL || pHead.next == NULL) return NULL;
    	ListNode slow = pHead;
    	ListNode fast = pHead;
    	while (fast && fast.next){
    		slow = slow.next;
    		fast = slow.next.next;
    		if (slow == fast){
    			break;
    		}
    	}
    	fast = pHead;
		while(fast != slow){
			fast = fast.next;
			slow = slow.next;
		}
		return
    }
};