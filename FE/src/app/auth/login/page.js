"use client";
import { DefaultButton } from "@/app/components/ui/buttons";
import { InputEnd, InputStart } from "@/app/components/ui/inputs";
import Link from "next/link";
import { FaGoogle, FaApple } from "react-icons/fa";
import { getPlayer, login, password } from "@/app/api";
import React, { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import localStorageManager from "@/utils/localStorageManager";
import { routes } from "@/app/api/routes";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const router = useRouter();

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = async () => {
    // try {
      // const data = await login({ email, password });
      // if (data) {
      //   if (data === "NOT VERIFIED") {
      //     router.push("/auth/unverified?email=" + email);
      //   } else {
      //     localStorageManager.setItem({ ...data }, "user");
      // router.push("/dashboard/main");
      //     }
      //   }
      // } catch (error) {
      //   alert(error.message);
      // }
    
    if (email.endsWith("@admin.it")) {
      router.push("/dashboard/admin");
    } else if (email.endsWith("@cliente.it")) {
      router.push("/dashboard/cliente");
    } else {
      alert("Email domain not recognized");
    }
  };

  return (
    <div className="w-full max-w-md p-8 space-y-8 bg-light-background border-[0.2px] rounded shadow dark:bg-dark-background  dark:border-dark-border">
      <h2 className="text-2xl font-bold text-center text-light-text dark:text-dark-text">
        Login
      </h2>
      <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
        <input type="hidden" name="remember" value="true" />
        <div className="rounded-md shadow-sm -space-y-px">
          <InputStart
            type={"Email"}
            placeholder={"Email"}
            label={"Email address"}
            value={email}
            onChange={handleEmailChange}
          />
          <InputEnd
            type={"password"}
            placeholder={"Password"}
            label={"Password"}
            value={password}
            onChange={handlePasswordChange}
          />
        </div>

        <div className="flex items-center justify-between">
          <div className="text-sm">
            <Link href="/auth/forgot">Forgot your password?</Link>
          </div>
        </div>

        <div>
          <DefaultButton text={"Login"} onClick={handleSubmit} />
        </div>
      </form>
      <div className="text-sm text-center">
        <Link href="/auth/signup">Don't have an account? Sign Up</Link>
      </div>
    </div>
  );
}
