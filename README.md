# Nolan_Clone
Basic Features(The overall AIM) :-


    1)Login(Google,Facebook,Email)

    
        Google:-
        Email:-
    2)DashBoard:-Name  and all the scripts under that user

    
    3)Create Script tab(it sould take1)Title,2)Plot,3)Genre as input and generate:-

    
                            1)Atleast 4 scenes along with thier titlles,

                            
                            2)List of Characters

                            
                            3)A title page(wwith title,copyright(according to screenplay standards

                            
                            4)allow for version controool of the Scripts saved versions)))

                            
    3)AI integrated Script generator(-Autofill fields  with a pdf maybe,

    
                                    -Ask AI change accent, continue dialogue, change ton of text
                                    -AI Image Generations,Draw Scenes and Characters
                                    -Screenplay Title Generations
                                    -Script Smart,Automatically format text into a screenplay format
                                    -Create Scene,Import your scene's beat sheet and let Nolan generate the initial draft of your scene.
                                    -Break Smart,Screenplay Breakdown and summary)

                                    
    4)make it offline capable

    
    5)Ensure data is all data is secure and encrypted 

    

Models:-


    UserProfile=

    
        -Email(Everytime one successfully logs in,check if the user already exists,if not create a new user profile)
        -Scripts(List Data Structure)

        
    Scripts:-

    
        -id:-unique
        -Title-Text
        -Scenes-List Data Structure
        -Characters-List Data Structure
        PDF converted in the format

        

References:-
    For  login

    
        https://medium.com/@namantam1/login-with-facebook-and-google-in-django-using-social-auth-app-django-d042bfeb04cb
        https://github.com/namantam1/social-auth-app-django/tree/master
        https://www.nolanai.app/
        https://webkul.com/blog/how-to-generate-facebook-app-id/
        https://getbootstrap.com/docs/5.3/components/navbar/

        
    for ChatGpt Integration:-

    
        https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key
        https://levelup.gitconnected.com/how-we-integrated-chatgpt-to-our-django-project-ca95ea50d371
        https://www.geeksforgeeks.org/how-to-implement-chatgpt-in-django/
        https://blog.devgenius.io/how-to-implement-chat-gpt-in-django-d741fc8f27de
        https://platform.openai.com/docs/quickstart/closing

        
# Scene headings (Location and Time)
scene_headings = [
    "INT. ABANDONED ART STUDIO - DAY",
    "EXT. CITY STREETS - DAY",
    "INT. GOVERNMENT HEADQUARTERS - NIGHT",
    "INT. ABANDONED ART STUDIO - NIGHT",
    "EXT. CITY STREETS - CONTINUOUS",
    "INT. GOVERNMENT HEADQUARTERS - CONTINUOUS",
    "INT. ABANDONED ART STUDIO - CONTINUOUS"
]

# Action lines and character actions
action_lines = [
    "A dimly lit room filled with dusty canvases and broken sculptures. In the center, we find LARA (late 20s, pale and somber-looking) intently working on a mesmerizing painting of vibrant colors. She seems lost in her art, a sense of melancholy in her eyes.",
    "Suddenly, a faint sound echoes through the room. Lara looks around, puzzled. She notices a hidden compartment under an old wooden table and carefully opens it. Inside, she finds a GLIMMERING CRYSTAL. As she touches it, a surge of energy rushes through her body, causing her to stumble back.",
    "Lara picks up the shattered crystal fragments, realizing that her mission is accomplished.",
    "Determined, Lara starts showcasing her art in public spaces—parks, squares, and street corners. Each time she unveils a new piece, the crowd is captivated, and they start to feel the emotions emanating from the artwork. Slowly, a spark of life returns to their eyes.",
    "Word of Lara's miraculous art spreads like wildfire, reaching the ears of the emotionless government officials. They see her as a threat to their controlled society and decide to put an end to her subversive actions.",
    "During the chaos, the crystal falls to the ground, shattering into pieces.",
    "Amidst the chaos, Lara picks up the shattered crystal fragments, realizing that her mission is accomplished."
]

# Character names and dialogues
dialogues = [
    ("LARA", "(whispers) What is this?"),
    ("LARA", "(whispers) They need to experience this."),
    ("GOVERNMENT OFFICIAL 1", "(angry) We cannot let this disrupt the order we've established!"),
    ("GOVERNMENT OFFICIAL 2", "(determined) Capture her, and seize that artifact!"),
    ("LARA", "(smiling) Art has the power to change the world."),
    ("CITIZEN 1", "(teary-eyed) I remember... I can feel again!"),
    ("CITIZEN 2", "(excited) This is incredible!"),
    ("GOVERNMENT OFFICIAL 1", "(astonished) Is this what we've been missing all along?"),
    ("GOVERNMENT OFFICIAL 2", "(whispers) Maybe we were wrong...")
]

# Transitions
transitions = [
    "FADE OUT."
]

# Scene breakdown based on scene headings
scene_breakdown = {
    scene_headings[0]: [action_lines[0], dialogues[0]],
    scene_headings[1]: [action_lines[1], dialogues[1]],
    scene_headings[2]: [action_lines[4], dialogues[2], dialogues[3]],
    scene_headings[3]: [action_lines[3]],
    scene_headings[4]: [action_lines[5], dialogues[5], dialogues[6]],
    scene_headings[5]: [action_lines[6], dialogues[4], dialogues[7], dialogues[8]],
    scene_headings[6]: [action_lines[2], dialogues[9]],
}

# Shots (optional)
shots = {
    "INT. ABANDONED ART STUDIO - DAY": "MEDIUM SHOT of Lara painting her masterpiece.",
    "INT. ABANDONED ART STUDIO - NIGHT": "CLOSE-UP of shattered crystal fragments on the floor.",
    "EXT. CITY STREETS - DAY": "WIDE SHOT of Lara showcasing her art to the crowd.",
    "EXT. CITY STREETS - CONTINUOUS": "PAN SHOT of citizens experiencing emotions for the first time.",
}

# Print the screenplay in a structured format
for scene in scene_headings:
    print(scene)
    print(shots.get(scene, ""))  # Print optional shot description if available
    for line in scene_breakdown.get(scene, []):
        print(line)
    print("\n")
print(transitions[0])