import json
import re 
from langchain_community.llms import Ollama
from Rptopdf import Rptopdf # class to put it in pdf

class Ai_intface :
    def __init__(self):
        
        # Charger le JSON
        with open("C:\\Users\\USER\\Documents\\projet&code\\Python\\Learning-python-journey-\\article_finder\\json\\daily_tech.json", "r") as f:
            data = json.load(f)

        # Formater le prompt
        prompt = f"""You are a helpful assistant specialized in summarizing technology articles.

        You will be given the content of two technology news websites: TechCrunch and Ars Technica.

        Your task is to:

        Read through the titles and descriptions of the articles from both websites.

        Select the 6 articles that would be most interesting for a general technology enthusiast (e.g., articles about major product launches, AI innovations, scientific breakthroughs, security issues, or space tech).

        For each of these 6 selected articles:

        Provide the title of the article

        Indicate the source (TechCrunch or Ars Technica)
        Do NOT include any introductory sentence about the articles. Start directly with the content or the list of articles.
        Do not mention the user in any way. 

        Give a summary in 3–5 sentences, focusing on the key information and why it matters

        Do not include articles that are overly niche (like deep enterprise tech), pure opinion pieces, or short notices.

        ⚠️ Only output the selected summaries. Do not include your reasoning or internal thoughts. No 'Thought:', 'Answer:' or explanation.

        Input:  JSON :\n{json.dumps(data, indent=2)}"""

        # Appeler le modèle
        llm = Ollama(model="deepseek-r1:14b")
        response = llm.invoke(prompt)
        #using regex to delete the thinking
        response = re.sub(r'<think>.*?</think>', '', response, flags=re.DOTALL)
        print(response)
        Rptopdf(response)