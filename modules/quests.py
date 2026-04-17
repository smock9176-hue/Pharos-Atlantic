# Quest System Implementation

class Quest:
    def __init__(self, quest_name, description):
        self.quest_name = quest_name
        self.description = description
        self.completed = False

    def complete_quest(self):
        self.completed = True
        print(f"Quest '{self.quest_name}' completed!")

    def __str__(self):
        return f"Quest: {self.quest_name}, Description: {self.description}, Completed: {self.completed}"

class QuestSystem:
    def __init__(self):
        self.quests = []

    def add_quest(self, quest):
        self.quests.append(quest)
        print(f"Quest '{quest.quest_name}' added.")

    def complete_quest(self, quest_name):
        for quest in self.quests:
            if quest.quest_name == quest_name:
                quest.complete_quest()
                return
        print(f"Quest '{quest_name}' not found.")

    def show_quests(self):
        for quest in self.quests:
            print(quest)