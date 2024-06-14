import type { NextRequest } from 'next/server';
import { authMiddleware } from "./middlewares/authMiddleware";

export function middleware(request: NextRequest) {
  if (!request.nextUrl.pathname.startsWith('/auth')) {
    return authMiddleware(request);
  }
}

export const config = {
  matcher: [
    '/((?!api|_next/static|_next/image|.*\\.png$).*)',
  ],
}
