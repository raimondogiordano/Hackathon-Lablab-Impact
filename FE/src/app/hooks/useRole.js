"use client";

import localStorageManager from "@/utils/localStorageManager";

const useRole = () => {
  const user = localStorageManager.getItem("user");

  const isAdmin = user?.roles?.includes("admin");

  return {
    isAdmin,
  };
};

export default useRole;
