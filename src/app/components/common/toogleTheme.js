"use client";
import useTheme from "@/app/hooks/useTheme";
import React from "react";
import { RoundedSwitch } from "../ui/switches";

function ToogleTheme({ theme, toggleTheme, sidebar }) {
  return (
    <div className={`flex items-center ${sidebar ? "ml-4" : ""}`}>
      <span className="text-[6px] opacity-80 mr-1">
        {(theme === "light" ? "dark" : "light").toUpperCase()}
      </span>
      <RoundedSwitch checked={theme === "dark"} onChange={toggleTheme} />
    </div>
  );
}

export default ToogleTheme;
