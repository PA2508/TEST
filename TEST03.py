def main():
    # Initialize variables
    scores = []
    num_scores = 10

    # Input 10 test scores
    for i in range(num_scores):
        score = float(input(f"Enter score #{i + 1}: "))
        scores.append(score)

    # Print highest and lowest scores
    highest = max(scores)
    lowest = min(scores)
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")

    # Print average of the scores
    average = sum(scores) / num_scores
    print(f"Average score: {average:.2f}")

    # Print the second largest score
    sorted_scores = sorted(scores, reverse=True)
    second_largest = sorted_scores[1]
    print(f"Second largest score: {second_largest}")

    # Check for scores greater than 100
    for score in scores:
        if score > 100:
            print("Warning: One or more scores are greater than 100.")

    # Drop the two lowest scores and calculate the average of the rest
    sorted_scores = sorted(scores)
    dropped_scores = sorted_scores[2:]  # Drop the two lowest scores
    average_without_lowest_two = sum(dropped_scores) / (num_scores - 2)
    print(f"Average without the two lowest scores: {average_without_lowest_two:.2f}")

if __name__ == "__main__":
    main()
