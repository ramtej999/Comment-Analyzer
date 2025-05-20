from deep_translator import GoogleTranslator

def translate_comments(comments): # Initialize translator to auto-detect and convert to English
    translator = GoogleTranslator(source="auto", target="en")
    translated_comments = []
    
    for comment in comments:
        try: # Translate each comment and append to the list
            # Set a timeout for translation to prevent long waits
            translated_comment = translator.translate(comment, timeout=10)  # Set timeout
            translated_comments.append(translated_comment)
        except Exception as e:
            # Handle translation errors gracefully
            print(f"Translation failed for: {comment}\nError: {e}")
    
    return translated_comments
