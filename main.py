from extract_comments import extract_comments
from translate_comments import translate_comments
from summarize_comments import summarize_comments

def main():
    # Ask user to input URL
    video_url = input("Enter the URL of the video/page: ").strip()

    # Step 1: Extract comments dynamically
    comments = extract_comments(video_url)
    if not comments:
        print("No comments found or unable to extract comments.")
        return

    print("\nExtracted Comments:", comments)

    # Step 2: Translate comments
    translated_comments = translate_comments(comments)
    print("\nTranslated Comments:", translated_comments)

    # Step 3: Summarize comments
    summary = summarize_comments("\n".join(translated_comments))
    print("\nSummary of Comments:\n", summary)

if __name__ == "__main__":
    main()
