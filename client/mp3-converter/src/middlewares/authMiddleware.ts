import { NextResponse, type NextRequest } from 'next/server';

export function authMiddleware(request: NextRequest) {
  const currentUser = request.cookies.get('currentUser')?.value;
  if (!currentUser) {
    return NextResponse.redirect(new URL('/auth/login', request.url));
  }
  return NextResponse.next();
}
