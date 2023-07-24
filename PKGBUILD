# Maintainer: Joshua Ashton <joshua@froggi.es>
# Maintainer: Emil Velikov <emil.l.velikov@gmail.com>

pkgname=umr
epoch=1
pkgver=jupiter_extras_1.0.8
pkgrel=1
pkgdesc='userspace debugging and diagnostic tool for AMD GPUs using the AMDGPU kernel driver'
arch=('i686' 'x86_64')
url='https://lists.freedesktop.org/archives/amd-gfx/2017-February/005122.html'
license=('MIT')
depends=('libpciaccess' 'ncurses' 'llvm-libs')
makedepends=('git' 'cmake' 'llvm' 'libdrm')
source=('git+https://gitlab.freedesktop.org/tomstdenis/umr.git#commit=22a2a8c02af49badc19ba1e9fdb2834988933c5f')
sha256sums=('SKIP')

build() {
	mkdir -p build
	cd build
	cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=lib -DCMAKE_BUILD_TYPE=Release -DUMR_NO_GUI=ON ../umr
}

package() {
	cd build
	make DESTDIR="$pkgdir" install
	cd ../umr
	install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 LICENSE
}

