from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def main():
    print("Text Translation Program")

    # Get user input
    text_to_translate = input("Enter the text you want to translate: ")
    target_language = input("Enter the target language (e.g., 'es' for Spanish, 'fr' for French): ")

    # Perform translation
    translated_text = translate_text(text_to_translate, target_language)

    # Display the result
    print(f"\nOriginal text: {text_to_translate}")
    print(f"Translated text ({target_language}): {translated_text}")

if __name__ == "__main__":
    main()