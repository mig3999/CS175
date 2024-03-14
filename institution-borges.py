{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "05525818-8cf4-49a5-8b34-b2e54f59516f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "\n",
      " Welcome to Borges Technology Instition **twitch twitch**\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "name:        Miguel\n",
      "address:     qweqwe\n",
      "email:       qweqwe\n",
      "program:     qweqe\n",
      "student #:   902\n",
      "entry grade: 120\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ERROR.  PLEASE FIX IT\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "entry grade: -5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ERROR.  PLEASE FIX IT\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "entry grade: 121\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ERROR.  PLEASE FIX IT\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "entry grade: 75\n",
      "int status:  yes\n",
      "# courses:   5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "student: Miguel is accepted\n",
      "tuition: International Full-time = $7500\n"
     ]
    }
   ],
   "source": [
    "class Member:\n",
    "\n",
    "    def __init__(self, name, address, email, program):\n",
    "        self.name = name\n",
    "        self.address = address\n",
    "        self.email = email\n",
    "        self.program = program\n",
    "        \n",
    "class Faculty(Member):\n",
    "            def __init__(self, name, address, email, program, faculty_number):\n",
    "                super().__init__(name, address, email, program)\n",
    "                self.faculty_number = faculty_number\n",
    "                self.courses_teaching = []\n",
    "                \n",
    "\n",
    "class Student(Member):\n",
    "            def __init__(self, name, address, email, program, student_number, entry_grade, international):\n",
    "                super().__init__(name, address, email, program)\n",
    "                self.student_number = student_number\n",
    "                self.courses_taken = []\n",
    "                self.courses_current = []\n",
    "                self.entry_grade = entry_grade\n",
    "                self.international = international\n",
    "\n",
    "            def checkGrade(self):\n",
    "                if (self.entry_grade > 50):\n",
    "                    print (\"accepted\")\n",
    "                elif (self.entry_grade == 50):\n",
    "                    print (\"accepted, but needs support\")\n",
    "                else: \n",
    "                    print (\"No\")\n",
    "\n",
    "\n",
    "print(\"\\n\\n\\n Welcome to Borges Technology Instition **twitch twitch**\\n\")\n",
    "enterName =          input(\"name:       \")\n",
    "enterAddress =       input(\"address:    \")\n",
    "enterEmail =         input(\"email:      \")\n",
    "enterProgram =       input(\"program:    \")\n",
    "enterStudentNumber = input(\"student #:  \")\n",
    "\n",
    "enterGrade = \"none\"\n",
    "while (enterGrade == \"none\"):\n",
    "    enterGrade =         input(\"entry grade:\")\n",
    "    if (float(enterGrade) < 0) or (float(enterGrade) > 100):\n",
    "        enterGrade = \"none\"\n",
    "        print (\"ERROR.  PLEASE FIX IT\")\n",
    "        \n",
    "enterInternational = input(\"int status: \")\n",
    "enterTime =          input(\"# courses:  \")\n",
    "\n",
    "if (enterInternational == \"yes\"):\n",
    "    enterIntBoolean = True\n",
    "else:\n",
    "    enterIntBoolean = False\n",
    "\n",
    "student1 = Student(enterName, enterAddress, enterEmail, enterProgram, int(enterStudentNumber), float(enterGrade), enterIntBoolean)\n",
    "\n",
    "print (\"student:\", student1.name, \"is \", end=\"\")\n",
    "student1.checkGrade()\n",
    "\n",
    "if (student1.international == True):\n",
    "    if (int(enterTime) < 4):\n",
    "        print (\"tuition: International Part-Time = $3500\")\n",
    "    else:\n",
    "        print (\"tuition: International Full-time = $7500\")\n",
    "else:\n",
    "    if (int(enterTime) < 4):\n",
    "        print (\"tuition: Domestic Part-Time = $1800\")\n",
    "    else:\n",
    "        print (\"tuition: Domestic Full-time = $3500\")\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "03e437d8-d0e4-42a0-8e90-137a51cf629b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8fbebb0c-2e4c-48bf-9934-46df1d3ec108",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
