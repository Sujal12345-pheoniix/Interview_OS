import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "InterviewOS",
  description: "Next-gen AI interview operating system.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased bg-[#09090b]">
        {children}
      </body>
    </html>
  );
}
