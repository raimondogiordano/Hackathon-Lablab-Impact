"use client";
import React from "react";
import { LogoAuth } from "../ui/logos";
import ToogleTheme from "../common/toogleTheme";
import useTheme from "@/app/hooks/useTheme";

function AuthLayout({ children }) {
  const { theme, toggleTheme } = useTheme();
  return (
    <div className="relative">
      <LogoAuth theme={theme} />
      <div className="flex min-h-[calc(100dvh-100px)] h-[calc(100dvh-100px)] items-center justify-center bg-light-background dark:bg-dark-background">
        {children}
      </div>

      {/* Barra con il ToogleTheme allineato a destra */}
      <div className="absolute bottom-5 right-5">
        <ToogleTheme theme={theme} toggleTheme={toggleTheme} />
      </div>
    </div>
  );
}

export default AuthLayout;
