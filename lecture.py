{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter your nameaSif\n",
      "ASIF asif Asif\n",
      "enter your nameKamRAN\n",
      "('KAMRAN', 'kamran', 'Kamran')\n",
      "<class 'tuple'>\n"
     ]
    }
   ],
   "source": [
    "def convert(name):\n",
    "    return name.upper(), name.lower(), name.capitalize()\n",
    "\n",
    "theName = input(\"enter your name\")\n",
    "upper, lower, capital = convert(theName)\n",
    "print(upper, lower, capital)\n",
    "\n",
    "name2 = input(\"enter your name\")\n",
    "names2 = convert(name2)\n",
    "print(names2)\n",
    "print(type(names2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "inside function\n",
      "xy 20\n",
      "old value 10\n",
      "out of the function  10\n"
     ]
    }
   ],
   "source": [
    "\n",
    "z = 10\n",
    "xy = 20\n",
    "def sqr():\n",
    "    print(\"inside function\")\n",
    "    print(\"xy\", xy)\n",
    "    #xy = 10\n",
    "    print(\"old value\" ,z)\n",
    "\n",
    "z = 10\n",
    "sqr()\n",
    "print(\"out of the function \", z)    \n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "10\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "y = 20\n",
    "def whatever():\n",
    "    print(y)\n",
    "    x = y\n",
    "    #y = 2\n",
    "    print(y)\n",
    "\n",
    "y = 10\n",
    "whatever()\n",
    "print(y)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a city, or q to quit:Karachi\n",
      "It's one of the cleanest cities\n",
      "Enter a city, or q to quit:Honolulu\n",
      "It's one of the cleanest cities\n",
      "Enter a city, or q to quit:q\n"
     ]
    }
   ],
   "source": [
    "cleanest_cities = [\"Cheyenne\", \"Santa Fe\", \"Karachi\", \"Tucson\", \n",
    "                   \"Great Falls\", \"Honolulu\"]\n",
    "user_input = \"\"\n",
    "while user_input != \"q\":\n",
    "    user_input = input(\"Enter a city, or q to quit:\")\n",
    "    if user_input != \"q\":\n",
    "        if user_input in cleanest_cities:\n",
    "                print(\"It's one of the cleanest cities\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "---------    Patient Infor -----------         \n",
      "name :  Kamran Mansoor\n",
      "age :  age is not defined years\n",
      "---------    Patient Infor -----------         \n",
      "name :  zameer Ghazali\n",
      "age :  patient is 22 years old years\n",
      "---------    Patient Infor -----------         \n",
      "name :  amir Ansari\n",
      "age :  patient is 39 years old years\n"
     ]
    }
   ],
   "source": [
    "class Patient():\n",
    "    def __init__(self, fname, lname, age):\n",
    "        self.last_name = lname\n",
    "        self.first_name = fname\n",
    "        self.age = age\n",
    "        \n",
    "    def name(self):\n",
    "        return self.first_name + \" \"+ self .last_name\n",
    "    \n",
    "    def change_last_name(self, lname):\n",
    "        if (len(lname) >2):\n",
    "            self.last_name = lname\n",
    "            \n",
    "    def patient_info(self):\n",
    "        print(\"---------    Patient Infor -----------         \")\n",
    "        print(\"name : \", self.first_name + \" \" + self.last_name)\n",
    "        print(\"age : \", self.patient_age(), \"years\")\n",
    "        \n",
    "    def patient_age(self):\n",
    "        if self.age <= 0:\n",
    "            return \"age is not defined\"\n",
    "        else:\n",
    "            return \"patient is \" + str( self.age ) + \" years old\"\n",
    "\n",
    "pid4343 = Patient(\"amir\", \"Khan\", 39)\n",
    "pid4344 = Patient(\"zameer\", \"Ghazali\", 22)\n",
    "pid4345 = Patient(\"Kamran\", \"Mansoor\", 0)\n",
    "\n",
    "pid4343.last_name = \"Ansari\"\n",
    "#pid4343.last_name = \"xx\"\n",
    "pid4343.change_last_name(\"Ansari\")\n",
    "pid4343.change_last_name(\"xx\")\n",
    "\n",
    "#print(pid4343.name())\n",
    "#print(pid4344.name())\n",
    "#print(pid4343.age )\n",
    "#print(pid4343.patient_age())\n",
    "#print(pid4345.patient_age() )\n",
    "\n",
    "pid4345.patient_info() \n",
    "pid4344.patient_info() \n",
    "pid4343.patient_info() \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, world! \n",
      "file storage programming!\n",
      "\n"
     ]
    }
   ],
   "source": [
    "with open(\"e:/newfile.txt\", \"w\") as file:\n",
    "   file.write(\"Hello, world! \\n\")\n",
    "   file.write(\"file storage programming!\\n\")\n",
    "    \n",
    "with open(\"e:/newfile.txt\", \"r\") as f:\n",
    "    text_of_file = f.read()   \n",
    "    print(text_of_file)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class '_csv.reader'>\n",
      "submitted ['name', 'kamran', 'arif', 'noman']\n",
      "not submitted ['mazz', 'abaas']\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "with open(\"competitions.csv\") as f:\n",
    "    contents_of_file = csv.reader(f)\n",
    "    print(type(contents_of_file))\n",
    "    #print(contents_of_file[0])\n",
    "    submitted_names = []\n",
    "    not_submitted_names =[]\n",
    "    for each_line in contents_of_file:\n",
    "        #int(each_line)\n",
    "        if each_line[2]==\"not\":\n",
    "            \n",
    "            #print(each_line.index(\"mazz\"))\n",
    "            not_submitted_names.append(each_line[0] )\n",
    "        else:\n",
    "            submitted_names.append(each_line[0] )\n",
    "print(\"submitted\", submitted_names)\n",
    "print(\"not submitted\", not_submitted_names)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "each line values ['Year', 'Event', 'Winner']\n",
      "poter_compitition values ['Year', 'Event', 'Winner']\n",
      "each line values ['1995', 'Best-Kept Lawn', 'None']\n",
      "poter_compitition values ['Year', 'Event', 'Winner', '1995', 'Best-Kept Lawn', 'None']\n",
      "each line values ['1999', 'Gobstones', 'Welch National']\n",
      "poter_compitition values ['Year', 'Event', 'Winner', '1995', 'Best-Kept Lawn', 'None', '1999', 'Gobstones', 'Welch National']\n",
      "each line values ['2006', 'World Cup', 'Burkina Faso']\n",
      "poter_compitition values ['Year', 'Event', 'Winner', '1995', 'Best-Kept Lawn', 'None', '1999', 'Gobstones', 'Welch National', '2006', 'World Cup', 'Burkina Faso']\n"
     ]
    }
   ],
   "source": [
    "with open(\"competitions2.csv\") as f:\n",
    "    contents_of_file = csv.reader(f)\n",
    "    potter_competitions = []\n",
    "    for each_line in contents_of_file:\n",
    "        print(\"each line values\", each_line)\n",
    "        potter_competitions += each_line\n",
    "        print(\"poter_compitition values\", potter_competitions)\n",
    "\n",
    "#print()\n",
    "#print(potter_competitions[4])\n",
    "#index_number_of_target =potter_competitions.index(\"Best-Kept Lawn\")\n",
    "#print(index_number_of_target)    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the name of a competition:World Cup\n",
      "10\n",
      "11\n",
      "The winner was Burkina Faso\n"
     ]
    }
   ],
   "source": [
    "target = input(\"Enter the name of a competition:\")\n",
    "index_number_of_target = potter_competitions.index(target)\n",
    "print(index_number_of_target)\n",
    "index_number_of_winner = index_number_of_target + 1\n",
    "print(index_number_of_winner)\n",
    "\n",
    "the_winner = potter_competitions[index_number_of_winner]\n",
    "print(\"The winner was \" + the_winner)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "with open(\"newcompitition.csv\", \"w\", newline=\"\") as f:\n",
    "        data_handler = csv.writer(f)\n",
    "        data_handler = csv.writer(f, delimiter=',', quoting =csv.QUOTE_ALL)\n",
    "        # quote minimal is default,  escape character won't work\n",
    "        #data_handler = csv.writer(f, delimiter=',', quoting =csv.QUOTE_MINIMAL,  escapechar=\"`\")\n",
    "        #data_handler = csv.writer(f, delimiter=',', quoting =csv.QUOTE_NONE,  escapechar=\"\\\\\")\n",
    "        data_handler.writerow([\"Year\", \"Event\",\"Winner\"])\n",
    "        data_handler.writerow([\"1995\", \"Best-Kept, Lawn\", \"None\"])\n",
    "        data_handler.writerow([\"1999\", \"Gobstones\",\"Welch National\"])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"e:/newcompitition.csv\", \"a\", newline=\"\") as f:\n",
    "    data_handler = csv.writer(f, delimiter=\",\")\n",
    "    x = [\"2019\", \"Worldcup\", \"Asad\"]\n",
    "    data_handler.writerow(x)\n",
    "    data_handler.writerow([\"2006\", \"World Cup\", \"Burkina Faso\"])\n",
    "    data_handler.writerow([\"2011\", \"Butter Cup\", \"France\"])\n",
    "    data_handler.writerow([\"2012\", \"Coffee Cup\", \"Brazil\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "with open(\"json_file.json\", \"w\") as f:\n",
    "    \n",
    "    customer_29876 = {\"first name\": \"David\", \n",
    "                      \"last name\": \"Elliott\", \n",
    "                      \"address\": \"4803 Wellesley St.\"\n",
    "                     }\n",
    "    #customer_29877 = {\"first name\": \"vid\", \"last name\": \"Elli\",  \"address\": [\"fsdafdasfs\", \"fdasfsda\"]                     }\n",
    "\n",
    "    json.dump(customer_29876, f)\n",
    "    #json.dump(customer_29876, f)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'first name': 'David', 'last name': 'Elliott', 'address': '4803 Wellesley St.'}\n"
     ]
    }
   ],
   "source": [
    "with open(\"json_file.json\", \"r\") as f:\n",
    "    customer_29876 = json.load(f)\n",
    "    print(customer_29876)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What text file to open? json_file.json\n",
      "{\"first name\": \"David\", \"last name\": \"Elliott\", \"address\": \"4803 Wellesley St.\"}{\"first name\": \"David\", \"last name\": \"Elliott\", \"address\": \"4803 Wellesley St.\"}\n",
      "What text file to open? abcd.txt\n",
      "Sorry, abcd.txt not found.\n",
      "What text file to open? q\n",
      "Sorry, q not found.\n"
     ]
    }
   ],
   "source": [
    "filename = \"\"\n",
    "while filename !=\"q\":\n",
    "    try:\n",
    "        filename = input(\"What text file to open? \")\n",
    "        with open(filename) as f:\n",
    "            print(f.read())\n",
    "    except FileNotFoundError:\n",
    "        print(\"Sorry, \" + filename + \" not found.\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What text file to open? json_file.json\n",
      "{\"first name\": \"David\", \"last name\": \"Elliott\", \"address\": \"4803 Wellesley St.\"}\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    try:\n",
    "        filename = input(\"What text file to open? \")\n",
    "        if filename !=\"q\":\n",
    "            with open(filename) as f:\n",
    "                print(f.read())\n",
    "        break\n",
    "    except FileNotFoundError:\n",
    "        print(\"Sorry, \" + filename + \" not found.\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 Fiction,2 nonFiction, 9 = quit  (1/2)2\n",
      "What GenreArts\n",
      "location of   Arts  is  G\n",
      "1 Fiction,2 nonFiction, 9 = quit  (1/2)9\n"
     ]
    }
   ],
   "source": [
    "def searchDict(dct,genre):\n",
    "    genre = input(\"What Genre\")\n",
    "    for key, val in dct.items():\n",
    "        if key == genre:\n",
    "            print(\"location of  \", genre, \" is \", val)\n",
    "            break\n",
    "     #return \n",
    "fictions = {\"comedey\":\"A\", \"commic\":\"B\"}\n",
    "nonFiction = {\"History\":\"F\", \"Arts\":\"G\"}\n",
    "choice = \"\"\n",
    "while choice != 9:\n",
    "    choice = int( input(\"1 Fiction,2 nonFiction, 9 = quit  (1/2)\") )\n",
    "    if choice == 1:\n",
    "        searchDict(fictions)\n",
    "    elif choice== 2:\n",
    "        searchDict(nonFiction)\n",
    "        \n",
    "            \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}