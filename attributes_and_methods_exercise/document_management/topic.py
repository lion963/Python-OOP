class Topic:

    def __init__(self, id, topic, storage_folder):
        self.id = id
        self.topic = topic
        self.storage_folder = storage_folder

    def edit(self, new_topic, new_storage_folder):
        self.topic = new_topic
        self.storage_folder = new_storage_folder

    def __repr__(self):
        return f"Topic {self.id}: {self.topic} in {self.storage_folder}"


from attributes_and_methods_exercise.document_management.category import Category
from attributes_and_methods_exercise.document_management.document import Document
from attributes_and_methods_exercise.document_management.storage import Storage

c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)
