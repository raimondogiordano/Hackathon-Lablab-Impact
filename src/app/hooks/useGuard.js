"use client";

import { useEffect, useState } from "react";
import { usePathname } from "next/navigation";
import localStorageManager from "@/utils/localStorageManager";
import { useRouter } from "next/navigation";

const useGuard = () => {
  const pathname = usePathname();
  const router = useRouter();

  // useEffect(() => {
  //   try {
  //     verify();
  //   } catch (error) {
  //     alert("Sessione scaduta o non valida");
  //     router.replace("/auth/login");
  //   }
  // }, [pathname]);

  function parseJwt(token) {
    var base64Url = token.split(".")[1];
    var base64 = base64Url.replace(/-/g, "+").replace(/_/g, "/");
    var jsonPayload = decodeURIComponent(
      window
        .atob(base64)
        .split("")
        .map(function (c) {
          return "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2);
        })
        .join("")
    );

    return JSON.parse(jsonPayload);
  }

  const verify = () => {
    const user = localStorageManager.getItem("user");
    if (pathname) {
      if (!pathname.includes("auth")) {
        if (user) {
          const decoded = parseJwt(user.token);

          if (new Date().getTime() / 1000 >= decoded.exp) {
            localStorageManager.clear();
            throw new Error("Expired session");
          }
        } else {
          localStorageManager.clear();
          throw new Error("Expired session");
        }
      }
    }
  };

  return null;
};

export default useGuard;
