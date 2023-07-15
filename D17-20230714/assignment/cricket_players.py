cricket_players=[{"name":"M S Dhoni","No.of.Centuries":16,"No.of.Half centuries":136,"Wickets taken":1,"hat trick wickets":0,"Top batting score":224},
                 {"name":"AB Devilliers","No.of.Centuries":72,"No.of.Half centuries":169,"Wickets taken":11,"hat trick wickets":0,"Top batting score":278},
                 {"name":"Andre Russel","No.of.Centuries":76,"No.of.Half centuries":108,"Wickets taken":557,"hat trick wickets":7,"Top batting score":132},
                 {"name":"David Warner","No.of.Centuries":16,"No.of.Half centuries":136,"Wickets taken":10,"hat trick wickets":8,"Top batting score":335},
                 {"name":"Devon Conway","No.of.Centuries":29,"No.of.Half centuries":61,"Wickets taken":0,"hat trick wickets":6,"Top batting score":327}]

def player_statistics(cricket_players):

    for player in cricket_players:

        name=player["name"]
        centuries=player["No.of.Centuries"]
        hat_tricks=player["hat trick wickets"]
        top_score=player["Top batting score"]
        
        if player["No.of.Centuries"] > 10:
            print(f"{name}\n{centuries}")


        if player["hat trick wickets"]>5:
            print(f"{name}\n{hat_tricks}")
  
     
        print(f"{name}\n{top_score}")        

player_statistics(cricket_players)
