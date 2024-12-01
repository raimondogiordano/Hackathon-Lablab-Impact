"use client";

import React from "react";
import ChatPage from "../chat/page"; // Assicurati di avere il componente ChatPage importato

function Main() {

  return (
    <div className="p-4 h-screen">
      <div className="mb-4">
        <h1 className="text-2xl font-bold text-center">Proposte dei Quartieri</h1>
        <p className="text-center text-lg">Benvenuto nel sistema di supporto per le proposte di miglioramento dei quartieri. Chatta con noi per condividere le tue idee o ottenere informazioni!</p>
      </div>

      <div
        className="w-full h-3/4 bg-light-background dark:bg-dark-background text-light-text dark:text-dark-text p-4 border border-light-border dark:border-dark-border z-50 transition-all duration-500 ease-in-out overflow-y-auto"
      >
        <ChatPage />
      </div>

    </div>
  );
}

export default Main;
