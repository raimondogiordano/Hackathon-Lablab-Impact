import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Vox Populi",
  description: "Hackathon webApp",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={`${inter.className} max-w-[1920px] mx-auto px-4`}>
        {children}
      </body>
    </html>
  );
}
