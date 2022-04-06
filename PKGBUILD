# Contributor: Vicki Pfau <vi@endrift.com>
# Contributor: bartus <arch-user-repository@bartus.33mail.com>
# Contributor: Lars Hagström <lars@foldspace.nu>
# Contributor: Nephyrin Zey <nephyrin@doublezen.net>
# Contributor: John Schoenick <john@pointysoftware.net>
# Contributor: Geoffrey Teale <tealeg@googlemail.com>
pkgname=breakpad
pkgver=r1996.59abf117
pkgrel=2
pkgdesc="An open-source multi-platform crash reporting system"
arch=('i686' 'x86_64' 'armv7h')
url="https://chromium.googlesource.com/breakpad/breakpad/"
license=('BSD')
makedepends=('git')
depends=('gcc-libs')
provides=('google-breakpad')
source=('git+https://chromium.googlesource.com/breakpad/breakpad#commit=59abf117ac7a4b74b422ff27dddb33b819f18f2e'
        'git+https://chromium.googlesource.com/linux-syscall-support#commit=e1e7b0ad8ee99a875b272c8e33e308472e897660')
sha256sums=('SKIP'
            'SKIP')

prepare() {
  ln -sfT "$srcdir/linux-syscall-support" "$pkgname/src/third_party/lss"
}

pkgver() {
  cd "$srcdir/$pkgname"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  cd "$srcdir/$pkgname"

  echo "Configuring"
  autoreconf
  ./configure --prefix=/usr --libexecdir=/usr/lib
  echo "Building"
  make
}

package() {
  cd "$srcdir/$pkgname"
  make DESTDIR="$pkgdir" install
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
