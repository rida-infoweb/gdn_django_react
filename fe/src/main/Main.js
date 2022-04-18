import React, { Component } from "react";
 
import {
    Route,
    NavLink,
    BrowserRouter,
    Routes
  } from "react-router-dom";
import ChefFiliere from "./ChefFiliere";
import Enseignant from "./Enseignant";
import Etudiant from "./Etudiant";
import Matiere from "./Matiere";
import Note from "./Note";
import Parametre from "./Parametre"
import Accueil from "./Accueil"

class Main extends Component {
  render() {
    return (
        <BrowserRouter>
        <div>
          <h1 className="text-center">Gestion des Notes des étudiants GLCL</h1>
          <ul className="header">
          <li><NavLink exact to="/accueil">Accueil</NavLink></li>
          <li><NavLink exact to="/chefFiliere">Chef de filière</NavLink></li>
          <li><NavLink exact to="/enseignant">Enseignant</NavLink></li>
          <li><NavLink exact to="/etudiant">Étudiant</NavLink></li>
          <li><NavLink exact to="/matiere">Matière</NavLink></li>
          <li><NavLink exact to="/note">Note</NavLink></li>
          <li><NavLink exact to="/parametre">Paramètres</NavLink></li>
          </ul>
          <div className="content">
            <Routes>          
          <Route exact path="/accueil" element={<Accueil/>}/>
          <Route exact path="/chefFiliere" element={<ChefFiliere/>}/>
          <Route exact path="/enseignant" element={<Enseignant/>}/>
          <Route exact path="/etudiant" element={<Etudiant/>}/>
          <Route exact path="/matiere" element={<Matiere/>}/>
          <Route exact path="/note" element={<Note/>}/>
          <Route exact path="/parametre" element={<Parametre/>}/>
          </Routes>
          </div>
        </div>
        </BrowserRouter>
    );
  }
}
 
export default Main;