import json


def build_profile(name, grade, skills):
    return {
        "name": name,
        "grade": grade,
        "skills": skills,
        "is_beginner": grade == 1,
    }


def save_profile(profile, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)


def load_profile(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


name = input("你的名字：")
grade = int(input("你的年级（数字）："))
skills = ["Python", "Git", "VSCode"]

profile = build_profile(name, grade, skills)
save_profile(profile, "profile.json")

print("保存成功：")
print(load_profile("profile.json"))