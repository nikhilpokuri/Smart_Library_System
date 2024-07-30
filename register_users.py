from abstract_user import User


class Student:
    def register_student(self, name, branch):
        User.users_data["student"].append((name, branch))
        return f"Student {name} from {branch} Registered\n"


class Faculty:
    def register_faculty(self, name, branch):
        User.users_data["faculty"].append((name, branch))
        return f"{branch} Branch Faculty {name} Registered\n"


class UserAdapter(User):
    def __init__(self, name, branch, user_type):
        self.name = name
        self.branch = branch
        self.user_type = user_type
        self.__userSaver = {
            "student": Student().register_student,
            "faculty": Faculty().register_faculty,
        }

    def register_user(self):
        if self.user_type in self.__userSaver:
            print(self.__userSaver[self.user_type](self.name, self.branch))

    @staticmethod
    def get_users_data():
        print(User.users_data)
        return User.users_data


# s1 = UserAdapter("nick", "cse", "student")
# s2 = UserAdapter("steeve", "ece", "student")
# f1 = UserAdapter("tony", "cse", "faculty")
# f2 = UserAdapter("clint", "ece", "faculty")

# s1.register_user()
# s2.register_user()
# f1.register_user()
# f2.register_user()

# UserAdapter.get_users_data()
