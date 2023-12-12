# Jellyfish-ChatBot

Author: Nguyen Truong Son and Dinh Bao Minh

A e-commercial chatbot which helps answer product, promtion and related infomations of 6 retailers in Vietnam (Circle-K, Winmart, 7-Eleven, Aeon Mall, Lotte Mart, Top Market)

Jellyfish-Chatbot was built based on streamlit-chat API.
NLU module of Jellyfish-Chatbot using Information Extraction module public in [].
The answer then generated by Chat Completions API.

# Information Query Process

(chèn hình ảnh vô đây nhé :D)

-	1: User sends a question to Jellyfish-Chatbot;
-	2: Information Extraction module extracts tuple (h,r,t);
`where h is head entity, t is tail entity and r is relationship between them.`
-	3: Based on (h,r,t) extracted, a suitable Cypher will be used to query data from knowledge graph (KG);
KG was created following the paper []
-	4: The Knowledge Graph returns the desired data and sends it to Chat Completions API;
-	5: Chat Completions API generate appropriate answers;
-	6: Jellyfish-Chatbot displays the answer content built in Step 5.

#### References
**[1]** Minh DinhBao, Viet DangAnh and Loc NguyenThe, “Xây dựng Đồ thị tri thức Thương mại điện tử Tiếng Việt dựa trên Trích xuất thông tin ngữ nghĩa với BERT”, The 26th National Conference on Electronics, Communications and Information Technology, 2023.
