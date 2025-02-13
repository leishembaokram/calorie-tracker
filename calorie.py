class Exercise:
    def __init__(self, name, calories_burn_rate):
        self.name = name
        self.calories_burn_rate = calories_burn_rate

    def calculate_calories_burned(self, duration_or_sets):
        return self.calories_burn_rate * duration_or_sets


class CardioExercise(Exercise):
    def __init__(self, name, calories_burn_rate, cardio_type):
        super().__init__(name, calories_burn_rate)
        self.cardio_type = cardio_type


class WeightExercise(Exercise):
    def __init__(self, name, calories_burn_rate, weight_lifted):
        super().__init__(name, calories_burn_rate)
        self.weight_lifted = weight_lifted


class User:
    def __init__(self, weight, age):
        self.weight = weight
        self.age = age


class CalorieTracker:
    def __init__(self, user):
        self.user = user
        self.exercise_logs = []

    def log_exercise(self, exercise, duration_or_sets):
        calories_burned = exercise.calculate_calories_burned(duration_or_sets)
        self.exercise_logs.append((exercise.name, duration_or_sets, calories_burned))
        print(f"Logged {duration_or_sets} {exercise.name} - {calories_burned} calories burned.")

    def view_logs(self):
        print("\nExercise Logs:")
        for log in self.exercise_logs:
            print(f"{log[1]} {log[0]} - {log[2]} calories burned")

    def get_total_calories_burned(self):
        return sum(log[2] for log in self.exercise_logs)


# Example usage:
if __name__ == "__main__":
    # Create user
    user = User(weight=70, age=25)

    # Create exercises
    running = CardioExercise("Running", calories_burn_rate=10, cardio_type="Jogging")
    bench_press = WeightExercise("Bench Press", calories_burn_rate=5, weight_lifted=50)
    cycling = CardioExercise("Cycling", calories_burn_rate=8, cardio_type="Moderate")

    # Create tracker for the user
    tracker = CalorieTracker(user)

    # Log exercises
    tracker.log_exercise(running, duration_or_sets=30)
    tracker.log_exercise(bench_press, duration_or_sets=3)
    tracker.log_exercise(cycling, duration_or_sets=45)

    # View logs and get total calories burned
    tracker.view_logs()
    total_calories = tracker.get_total_calories_burned()
    print(f"\nTotal Calories Burned: {total_calories} calories")
