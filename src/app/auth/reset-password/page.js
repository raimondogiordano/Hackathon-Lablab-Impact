"use client";

import React, { useState, useEffect } from "react";
import { useSearchParams } from "next/navigation";
import { reset, verify, password as passwordReset } from "@/app/api";
import { InputEnd, InputStart } from "@/app/components/ui/inputs";
import Link from "next/link";
import { Suspense } from "react";
const ResetPassword = () => {
  const [loading, setLoading] = useState(true);
  const [verificationStatus, setVerificationStatus] = useState(null);
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [resetStatus, setResetStatus] = useState(null);
  const params = useSearchParams();
  const token = params.get("token");

  useEffect(() => {
    if (!token) return; // Assicurati che il token sia presente

    // Funzione simulata per verificare il token di reset password
    const verifyToken = async (token) => {
      try {
        setLoading(true);
        // Simuliamo una chiamata API per verificare il token
        if (!token) throw new Error("Token mancante");
        const response = await verify({ token });
        if (response.data.status) {
          setVerificationStatus("valid");
        } else {
          setVerificationStatus("invalid");
        }
      } catch (error) {
        setVerificationStatus("invalid");
      } finally {
        setLoading(false);
      }
    };

    verifyToken(token);
  }, [token]);

  const handleResetPassword = async (e) => {
    e.preventDefault();

    if (password !== confirmPassword) {
      setResetStatus("password_mismatch");
      return;
    }

    try {
      setLoading(true);

      // Simuliamo una chiamata API per resettare la password
      const response = await passwordReset({ token, password });
      if (response) {
        setResetStatus("success");
      } else {
        setResetStatus("error");
      }
    } catch (error) {
      setResetStatus("error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Suspense>
      <div className="flex flex-col items-center justify-start bg-light-background dark:bg-dark-background text-light-text dark:text-dark-text h-[60%] w-full">
        {loading ? (
          <div className="text-center">
            <p className="text-lg font-semibold">Verificando il token...</p>
            <div className="loader mt-4"></div>
          </div>
        ) : verificationStatus === "valid" ? (
          <div className="w-full max-w-md">
            <h2 className="text-2xl font-semibold mb-4 text-center">
              Reset Password
            </h2>
            {resetStatus === "password_mismatch" && (
              <p className="text-red-600 mb-4">
                Le password non corrispondono.
              </p>
            )}
            {resetStatus === "success" ? (
              <div>
                <p className="text-green-600 text-center">
                  La tua password è stata resettata con successo!
                </p>
                <div className="text-sm text-center">
                  <Link href="/auth/login">Back to Login</Link>
                </div>
              </div>
            ) : (
              <form onSubmit={handleResetPassword} className="w-full">
                <div className="w-full">
                  <InputStart
                    type="password"
                    value={password}
                    onChange={(e) => {
                      setPassword(e.target.value);
                      setResetStatus(null);
                    }}
                    placeholder={"Password"}
                    required
                  />
                  <InputEnd
                    type="password"
                    value={confirmPassword}
                    onChange={(e) => {
                      setConfirmPassword(e.target.value);
                      setResetStatus(null);
                    }}
                    placeholder={"Conferma Password"}
                    required
                  />
                </div>
                <button
                  type="submit"
                  className="w-full py-2 px-4 mt-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-accent-text bg-accent-background hover:bg-accent-background focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-accent-background"
                >
                  Resetta Password
                </button>
                <Link href="/auth/login">Back to Login</Link>
              </form>
            )}
            {resetStatus === "error" && (
              <p className="text-red-600 text-center mt-4">
                Si è verificato un errore. Per favore riprova.
              </p>
            )}
          </div>
        ) : (
          <div className="text-center">
            <p className="text-lg font-semibold text-red-600">
              Il token è invalido o scaduto. Per favore richiedi un nuovo reset
              della password.
            </p>
          </div>
        )}
      </div>
    </Suspense>
  );
};

export default ResetPassword;
