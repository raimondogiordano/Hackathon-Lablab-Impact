"use client";
import { reset } from "@/app/api";
import { DefaultButton } from "@/app/components/ui/buttons";
import { InputRounded } from "@/app/components/ui/inputs";
import Link from "next/link";
import { useState } from "react";

export default function ForgotPassword() {
  const [email, setemail] = useState("");
  const handleSubmit = async () => {
    try {
      await reset({ email });
    } catch (error) {
      alert(error.message);
    }
  };
  const handleChanges = (e) => {
    setemail(e.target.value);
  };
  return (
    <div className="w-full max-w-md p-8 space-y-8 border-light-border dark:border-dark-border border-[0.5px]">
      <h2 className="text-2xl font-bold text-center text-gray-900 dark:text-white">
        Forgot Password
      </h2>
      <form className="mt-8 space-y-6">
        <input type="hidden" name="remember" />
        <div className="rounded-md shadow-sm -space-y-px">
          <InputRounded
            onChange={handleChanges}
            placeholder={"Email"}
            value={email}
            label={"Email address"}
          />
        </div>

        <div>
          <DefaultButton text={"Send Reset Link"} onClick={handleSubmit} />
        </div>
      </form>
      <div className="text-sm text-center">
        <Link href="/auth/login">Back to Login</Link>
      </div>
    </div>
  );
}
