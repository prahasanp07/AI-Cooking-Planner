# LEVIT8 - AI-Cooking-Planner
Challenge:   A cooking to-do list  Build a simple AI micro-app that helps a user generate a personal cooking to-do list based on their day.  A structured meal planning flow that produces:  Breakfast/Lunch/Dinner plan  grocery list  Substitutions  budget feasibility logic

Live URL: https://levit8-cooking-planner.vercel.app/ 

+-----------------------------------------------------------------------+
|                             LEVIT8 ENGINE                             |
+-----------------------------------------------------------------------+
|                                                                        |
|  [⏰ Contextual Scheduling]  --->  Analyzes user's daily energy metrics|
|  [💰 Financial Guardrails]   --->  Real-time local grocery cost matching|
|  [🛒 Hyper-Local Checkout]   --->  Instant API cart-building (Instacart)|
|  [🔄 Dynamic Swap Logic]     --->  Waste reduction via smart substitutes|
|                                                                       |
+-----------------------------------------------------------------------+


### 🍳 1. Energy-Adaptive Menu Engineering
The platform maps meal complexity to your calendar stress. High-fatigue days automatically generate nutritious, low-standing-time dishes requiring less than 15 minutes of total prep, while low-stress days identify batch-cooking milestones.

### 🛒 2. Guardrailed Financial Logic & Dynamic Swaps
Our programmatic AI engine acts as a strict financial wall. If real-time, localized ingredient estimates breach your budget ceiling by even $1, the engine dynamically recalculates, substituting premium items with cost-effective, nutritionally equivalent staples to bring the target cost back under budget.

### 📋 3. Programmatic Interactive Checklist
Output elements are seamlessly injected as operational milestones. The app outputs an immediate grocery-to-kitchen to-do list with persistent state check-boxes, shifting text decoration to strike-through as you cross milestones off.

---

## 🛠️ Architecture & Tech Stack

Designed for blazing-fast edge speeds and immediate horizontal scalability:

* **Frontend Engine:** Single-page application layered with Tailwind CSS for a hyper-modern, minimalist dark tech theme (`#0E1117`).
* **Orchestration:** Built natively to run within AI-native workspaces (V0, Lovable, Replit Core, Antigravity Agent pipelines).
* **Intelligence Layer:** Deep orchestration via `gemini-2.5-flash` utilizing isolated system instruction parsing for deterministic Markdown structures and low-latency responses.

---

## 🚀 Rapid Local Deployment

Get the micro-app running locally in less than two minutes:

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/levit8-ai.git](https://github.com/your-username/levit8-ai.git)
   cd levit8-ai
Open the index file in your browser or run a simple local server.

Configure your API credentials inside your configuration profile or environment secrets block:

JavaScript
const GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE";
📈 Commercialization & Scale Strategy (Investor Roadmap)
Levit8 addresses the intersection of the $12B digital food-planning market and the wellness economy via a highly scalable, multi-layered monetization ecosystem:

B2B2C Checkout Affiliate Integration (Primary Driver): Single-click checkout pipelines routing the "Floating Grocery List" straight into local delivery network carts (Instacart, Amazon Fresh, Walmart Grocery), capturing a 2% - 5% commission wrapper on automated checkouts.

Levit8 Pro SaaS Tier: Premium subscription matrices unlocking macro-tracking syncs (Apple Health, MyFitnessPal) and predictive automated pantry memory to further suppress ingredient costs.

Data-Driven CPG Sponsorships: Contextual, native brand integrations inside the "Smart Substitutions" card array offering active promotional alternatives to the user.
