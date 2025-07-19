class s():
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Reverse String is ",self.name[::-1])
name=input("Enter any string")

st=s(name)
st.display()