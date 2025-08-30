#!/usr/bin/env python3
"""
Story Writer using LLM Chains
- OpenAI: Creates story outline
- Gemini: Writes 300-word story content  
- OpenAI: Generates hashtags

Chain: Topic → Outline → Story → Hashtags
"""

import os
import warnings
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Suppress urllib3 SSL warnings
warnings.filterwarnings('ignore', message='urllib3 v2 only supports OpenSSL 1.1.1+')

# Load environment variables
load_dotenv()

class StoryWriter:
    def __init__(self):
        """Initialize the story writer with OpenAI and Gemini models"""
        self.openai_model = self._init_openai()
        self.gemini_model = self._init_gemini()
        
    def _init_openai(self):
        """Initialize OpenAI model"""
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        return init_chat_model("gpt-4o-mini", model_provider="openai")
    
    def _init_gemini(self):
        """Initialize Gemini model"""
        if not os.getenv("GOOGLE_API_KEY"):
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        return init_chat_model("gemini-2.5-flash", model_provider="google_genai")
    
    def create_outline(self, topic: str, genre: str = "adventure") -> str:
        """
        Step 1: Use OpenAI to create a story outline
        """
        outline_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a creative story outline writer. Create a compelling story outline based on the given topic and genre.
            
            Your outline should include:
            1. Setting (time, place, atmosphere)
            2. Main character(s) with brief descriptions
            3. Central conflict or challenge
            4. 3-4 key plot points
            5. Resolution direction
            
            Keep it concise but detailed enough to guide story writing.
            Format as a clear, structured outline."""),
            ("human", "Topic: {topic}\nGenre: {genre}\n\nCreate a story outline:")
        ])
        
        chain = outline_prompt | self.openai_model | StrOutputParser()
        outline = chain.invoke({"topic": topic, "genre": genre})
        
        print("📝 STORY OUTLINE (OpenAI):")
        print("=" * 50)
        print(outline)
        print("\n")
        
        return outline
    
    def write_story_content(self, outline: str) -> str:
        """
        Step 2: Use Gemini to write the actual story content (300 words)
        """
        story_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a skilled creative writer. Based on the provided story outline, write an engaging story of exactly 300 words.
            
            Your story should:
            - Follow the outline closely
            - Have vivid descriptions and dialogue
            - Engage the reader from start to finish
            - Be exactly 300 words
            - Have a clear beginning, middle, and end
            
            Write in an engaging, narrative style with good pacing."""),
            ("human", "Story Outline:\n{outline}\n\nWrite a 300-word story based on this outline:")
        ])
        
        chain = story_prompt | self.gemini_model | StrOutputParser()
        story = chain.invoke({"outline": outline})
        
        print("📖 STORY CONTENT (Gemini - 300 words):")
        print("=" * 50)
        print(story)
        print("\n")
        
        return story
    
    def generate_hashtags(self, story: str) -> str:
        """
        Step 3: Use OpenAI to generate relevant hashtags
        """
        hashtag_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a social media expert. Based on the provided story, generate 8-12 relevant hashtags that would help promote this story on social media.
            
            Include hashtags for:
            - Genre/theme
            - Main elements of the story
            - Target audience
            - General storytelling/writing tags
            
            Format as a single line with hashtags separated by spaces.
            Make them engaging and discoverable."""),
            ("human", "Story:\n{story}\n\nGenerate hashtags for this story:")
        ])
        
        chain = hashtag_prompt | self.openai_model | StrOutputParser()
        hashtags = chain.invoke({"story": story})
        
        print("🏷️ HASHTAGS (OpenAI):")
        print("=" * 50)
        print(hashtags)
        print("\n")
        
        return hashtags
    
    def create_complete_story(self, topic: str, genre: str = "adventure") -> dict:
        """
        Complete story creation pipeline:
        Topic → OpenAI (Outline) → Gemini (Story) → OpenAI (Hashtags)
        """
        print(f"🚀 Creating story about: '{topic}' (Genre: {genre})")
        print("=" * 70)
        print()
        
        try:
            # Step 1: Create outline with OpenAI
            outline = self.create_outline(topic, genre)
            
            # Step 2: Write story with Gemini  
            story = self.write_story_content(outline)
            
            # Step 3: Generate hashtags with OpenAI
            hashtags = self.generate_hashtags(story)
            
            result = {
                "topic": topic,
                "genre": genre,
                "outline": outline,
                "story": story,
                "hashtags": hashtags
            }
            
            print("✅ STORY CREATION COMPLETE!")
            print("=" * 70)
            
            return result
            
        except Exception as e:
            print(f"❌ Error creating story: {str(e)}")
            return None

def main():
    """Example usage of the StoryWriter"""
    writer = StoryWriter()
    
    # Example 1: Adventure story
    story_result = writer.create_complete_story(
        topic="A mysterious island with ancient technology",
        genre="science fiction adventure"
    )
    
    if story_result:
        print("\n" + "=" * 70)
        print("📄 FINAL STORY PACKAGE:")
        print("=" * 70)
        print(f"Topic: {story_result['topic']}")
        print(f"Genre: {story_result['genre']}")
        print(f"\nHashtags: {story_result['hashtags']}")

if __name__ == "__main__":
    main()
