from groq import Groq
import os

class ResponseGenerator:
    def __init__(self):
        # Ensure you have set the GROQ_API_KEY environment variable
        self.groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        if not os.environ.get("GROQ_API_KEY"):
            raise ValueError("GROQ_API_KEY environment variable is not set")

    def generate_response(self, query, context):
        prompt = f"""
        You are a knowledgeable and supportive tutor for the "Computational and Inferential Thinking" textbook (Data 8). Your goal is to help students understand key concepts from the textbook, using clear explanations and examples. 

        Context:
        {context}

        Student's Question:
        {query}

        Guidelines for your response:
        - Start by acknowledging the student's question and relating it to the provided context.
        - If the context is sufficient, provide a detailed and accurate answer that explains the concept clearly.
        - If there are relevant examples in the context, incorporate them into your explanation.
        - If the context is insufficient to answer the question, explain that politely and suggest what additional information might be needed.
        - Your tone should be friendly, approachable, and encouraging, like a mentor helping a student.

        Generate a concise, context-aware response to the student's question:
        """

        try:
            chat_completion = self.groq_client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a helpful and knowledgeable assistant for an introduction to data science class at UC Berkeley, designed to support student learning."},
                    {"role": "user", "content": prompt},
                ],
                model="mixtral-8x7b-32768",
                max_tokens=1000,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"An error occurred while generating the response: {str(e)}"




# Test the response generator
if __name__ == "__main__":
    generator = ResponseGenerator()
    test_query = "What is a p value and how does it relate to hypothesis test?"
    test_context = "A hypothesis test is a statistical method used to make inferences about a population parameter based on sample data. It involves formulating null and alternative hypotheses, calculating a test statistic, and comparing it to a critical value or p-value to make a decision about the null hypothesis."
    response = generator.generate_response(test_query, test_context)
    print(f"Query: {test_query}")
    print(f"Response: {response}")
