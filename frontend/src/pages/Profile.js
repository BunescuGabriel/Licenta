import Header from "../components/Header";
import React from "react";
import Profil from "../components/profile/Profil";
import Address from "../components/profile/Address";

const Home = () => {
    return (
        <div>
             <Header />
      <Profil />
      <Address />
        </div>

    );
}

export default Home;