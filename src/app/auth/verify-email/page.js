"use client";
import React, { useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";
import { verify } from "@/app/api";
import { Suspense } from "react";
function VerifyMail() {
  const [loading, setLoading] = useState(true);
  const [verificationStatus, setVerificationStatus] = useState(null);
  const params = useSearchParams();
  const token = params.get("token"); // Ottieni il token dal percorso URL

  useEffect(() => {
    const verifyEmail = async (token) => {
      try {
        if (!token) throw new Error("Token mancante");
        const response = await verify({ token });

        setLoading(true);
        if (response.data.status) {
          if (response.status === 202) {
            setLoading(false);
            setVerificationStatus("already");
          } else {
            setLoading(false);
            setVerificationStatus("success");
          }
        } else {
          setLoading(false);
          setVerificationStatus("error");
        }
      } catch (error) {
        setLoading(false);
        setVerificationStatus("error");
      }
    };

    verifyEmail(token);
  }, [token]);

  return (
    <Suspense>
      <div className="flex flex-col items-center justify-center  bg-light-background dark:bg-dark-background text-light-text dark:text-dark-text">
        {loading ? (
          <div className="text-center">
            <p className="text-lg font-semibold">Verificando la tua email...</p>
            <div className="loader mt-4"></div>{" "}
            {/* Placeholder per un'animazione di caricamento */}
          </div>
        ) : verificationStatus === "success" ? (
          <div className="text-center">
            <p className="text-lg font-semibold text-green-600">
              Verifica dell'email avvenuta con successo!
            </p>
          </div>
        ) : verificationStatus === "already" ? (
          <div className="text-center">
            <p className="text-lg font-semibold text-green-600">
              Email già verificata!
            </p>
          </div>
        ) : (
          <div className="text-center">
            <p className="text-lg font-semibold text-red-600">
              La verifica dell'email è fallita. Il token potrebbe essere scaduto
              o invalido.
            </p>
          </div>
        )}
      </div>
    </Suspense>
  );
}

export default VerifyMail;
