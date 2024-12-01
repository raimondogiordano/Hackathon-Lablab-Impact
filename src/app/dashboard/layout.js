"use client";
import React from "react";
import { LogoHeader } from "../components/ui/logos";
import useTheme from "../hooks/useTheme";
import ToogleTheme from "../components/common/toogleTheme";
import { useRouter } from "next/navigation";
import useGuard from "../hooks/useGuard";
import localStorageManager from "@/utils/localStorageManager";

const Layout = ({ children }) => {
  const router = useRouter();
  const { theme, toggleTheme } = useTheme();
  useGuard();

  const handleClickLogout = () => {
    localStorageManager.clear();
    router.replace("/auth/login");
  };

  return (
    <div className="flex min-h-screen bg-light-background dark:bg-dark-background text-light-text dark:text-dark-text">
      <div className="flex-1 flex flex-col">
        <header className="flex items-center justify-between p-4 border-b border-light-border dark:border-dark-border">
          <LogoHeader theme={theme} />
        </header>
        <main className="flex-1 p-4">
          {/* Contenuto principale */}
          {children}
        </main>

        {/* Barra con bottoni per logout e cambio tema */}
        <div className="flex justify-between items-center p-4 border-t border-light-border dark:border-dark-border">
          <ToogleTheme theme={theme} toggleTheme={toggleTheme} />
          <button
            onClick={handleClickLogout}
            className="bg-accent-background text-white py-2 px-4 rounded-lg"
          >
            Logout
          </button>
          
        </div>
      </div>
    </div>
  );
};

export default Layout;
