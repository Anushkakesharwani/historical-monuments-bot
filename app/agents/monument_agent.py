# app/agents/monument_agent.py

class MonumentAgent:
    # A simple knowledge base of monuments
    knowledge_base = {
        "taj mahal": "Taj Mahal is a stunning white marble mausoleum in Agra, India. It’s a UNESCO World Heritage Site.",
        "great wall": "The Great Wall of China spans over 13,000 miles and was built to protect China from invasions.",
        "colosseum": "The Colosseum in Rome is an iconic symbol of ancient Roman engineering and gladiatorial combat.",
    }

    def get_response(self, query):
        # Check if any monument keyword is in the query
        query = query.lower()
        for monument, fact in self.knowledge_base.items():
            if monument in query:
                return fact
        # Default response if nothing specific is found
        return "I can help with information on historical monuments. Ask me about any famous site!"
