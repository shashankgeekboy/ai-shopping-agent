# 🛍️ AI Shopping Agent

AI Shopping Agent is a virtual assistant designed to enhance the online shopping experience.  
It helps users search for fashion products across multiple platforms, apply discounts, estimate shipping times, compare prices, and check return policies. 🚀

---

## 📌 Features:
✅ **Product Search** – Finds products based on user input and preferences.  
✅ **Shipping Estimation** – Calculates shipping costs and estimated delivery times.  
✅ **Discount Checking** – Validates promo codes and applies discounts.  
✅ **Competitor Price Comparison** – Compares product prices from different e-commerce platforms.  
✅ **Return Policy Checking** – Fetches return policy details from various online stores.

---

## 🚀 Task Breakdown:

1. **Task A: Basic Item Search + Price Constraint**  
   - **User Query:** “Find a floral skirt under $40 in size S. Is it in stock, and can I apply a discount code ‘SAVE10’?”
   - **Steps:** Searches for the product, applies discount, checks availability.

2. **Task B: Shipping Deadline**  
   - **User Query:** “I need white sneakers (size 8) for under $70 that can arrive by Friday.”
   - **Steps:** Searches for sneakers and estimates shipping cost and arrival date.

3. **Task C: Competitor Price Comparison**  
   - **User Query:** “I found a ‘casual denim jacket’ at $80 on SiteA. Any better deals?”
   - **Steps:** Compares product prices across multiple e-commerce platforms.

4. **Task D: Returns & Policies**  
   - **User Query:** “I want to buy a cocktail dress from SiteB, but only if returns are hassle-free. Do they accept returns?”
   - **Steps:** Checks return policy for the product on SiteB.

5. **Task E: Multi-turn Interaction**  
   - **User Query:** “Find a floral skirt under $40 in size S. Can I apply a discount code and get shipping details?”
   - **Steps:** Combines search, discount, and shipping estimations in one response.

---

## 📚 Comparative Conceptual Map:
This section should summarize the key approaches discussed in the research papers. 
- **ReAct**: Synergizing reasoning and acting in language models.
- **Toolformer**: Teaching language models to use tools autonomously.
- **Chain of Tools**: Multi-tool learning using language models.
- **Language Agent Tree Search**: Unifying reasoning, acting, and planning for better tool usage.

---

## 📝 Short Written Analysis:
A short analysis of the methods used and their performance:
- **ReAct**: Excellent in combining reasoning and acting to perform tasks with multiple steps.
- **Toolformer**: Allows the model to self-learn, but could struggle in complex, real-time tasks.
- **Chain of Tools**: Provides great multi-step reasoning, but can be computationally expensive.

---

## 🛠️ Design Decisions:
- **Agent Architecture**: A simple decision tree for selecting tools based on user query.
- **Tool Selection**: Tools were selected based on user needs such as product search, shipping, price comparison, and return policies.
- **Reasoning**: Simple logic to decide which tool to invoke based on keywords in the query.

---

## ⚙️ Challenges & Improvements:
- **Challenges Faced**:
  - Integrating multiple tools for seamless interaction was challenging.
  - Ensuring the discount and price comparison tools provided accurate data.
- **Future Improvements**:
  - **AI Improvements**: More intelligent agent decision-making based on user history and preferences.
  - **Tool Expansion**: Integrating additional e-commerce platforms and advanced tools for personalization.

---

## 📜 Open Questions & References:
- **Open Questions**: How to improve the scalability of the tool usage? Can we make the reasoning process more adaptable in real-time?
- **References**:  
  1. **ReAct**: Synergizing reasoning and acting in language models.
  2. **Toolformer**: Language Models Can Teach Themselves to Use Tools.
  3. **ReST meets ReAct**: Self-improvement for multi-step reasoning LLM agent.
  4. **Chain of Tools**: Large language model is an automatic multi-tool learner.
  5. **Language Agent Tree Search**: Unifies reasoning, acting, and planning in language models.
