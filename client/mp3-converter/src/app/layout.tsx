import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { constants } from "@/app/utils/constants";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: constants.APP_NAME,
  description: "Converts video file into audio file",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  );
}
