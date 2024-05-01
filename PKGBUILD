# Maintainer: Andres Rodriguez <andresx7@gmail.com>
# Contributor: Luis Martinez <luis dot martinez at tuta dot io>

pkgname=gpu-trace
pkgver=2.13
pkgrel=1
pkgdesc="GPU Trace capture tool"
arch=('any')
url="https://github.com/lostgoat/gpu-trace"
license=('MIT')
depends=('python3' 'trace-cmd' 'perf')
provides=('amdgpu-trace')
conflicts=('amdgpu-trace')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('3ca8dee6089516faefd55710d848f8a3d1984f0032749711fccdc98e3570d13c')

#source=('gpu-trace::git+https://github.com/lostgoat/gpu-trace')

package() {
    install=gpu-trace.install
    cd "$pkgname-$pkgver"
    install -dm755 "$pkgdir/usr/bin/"
    make INSTALL_ROOT="$pkgdir" INSTALL_PREFIX="/usr/" install
    install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
    install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname/"
}
