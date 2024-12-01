"use client";
import { resendVerify } from "@/app/api";
import React, { useState } from "react";
import { useSearchParams } from "next/navigation";
import { useRouter } from "next/navigation";
const UnverifiedUserPage = () => {
  const [resendStatus, setResendStatus] = useState(null);
  const [loading, setLoading] = useState(false);
  const params = useSearchParams();
  const email = params.get("email");
  const router = useRouter();
  const handleResendEmail = async () => {
    try {
      setLoading(true);
      setResendStatus(null);

      // Simuliamo una chiamata API per reinviare l'email di verifica
      const response = resendVerify({ email: email });
      if (response) setResendStatus("success");
    } catch (error) {
      setResendStatus("error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center bg-light-background dark:bg-dark-background text-light-text dark:text-dark-text p-4">
      <div className="w-full max-w-md text-center">
        <h2 className="text-2xl font-semibold mb-4">
          Verifica il tuo indirizzo email
        </h2>
        <p className="mb-6">
          Grazie per esserti registrato! Abbiamo inviato un'email di verifica al
          tuo indirizzo. Per favore, controlla la tua casella (anche nello spam)
          di posta e clicca sul link di verifica per attivare il tuo account.
        </p>
        {resendStatus === "success" && (
          <p className="text-green-600 mb-4">
            Email di verifica inviata con successo!
          </p>
        )}
        {resendStatus === "error" && (
          <p className="text-red-600 mb-4">
            Si è verificato un errore. Per favore riprova.
          </p>
        )}
        <button
          onClick={handleResendEmail}
          disabled={loading}
          className="w-full py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-accent-text bg-accent-background hover:bg-accent-background focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-accent-background disabled:opacity-50"
        >
          {loading ? "Invio in corso..." : "Reinvia Email di Verifica"}
        </button>

        <button
          onClick={() => router.replace("/auth/login")}
          disabled={loading}
          className="w-full mt-2 py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-accent-text bg-accent-background hover:bg-accent-background focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-accent-background disabled:opacity-50"
        >
          Torna alla login
        </button>
      </div>
    </div>
  );
};

export default UnverifiedUserPage;
