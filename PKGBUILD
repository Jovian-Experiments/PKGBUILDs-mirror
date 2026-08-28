# Maintainer: Andres Rodriguez <andresx7@gmail.com>
# Contributor: Luis Martinez <luis dot martinez at tuta dot io>

pkgname=gpu-trace
pkgver=2.16
pkgrel=1.1
pkgdesc="GPU Trace capture tool"
arch=('any')
url="https://github.com/lostgoat/gpu-trace"
license=('MIT')
depends=('python>=3.14' 'python<3.15' 'trace-cmd' 'perf')
provides=('amdgpu-trace')
conflicts=('amdgpu-trace')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('34c614616611b61258619bd96209452a3ac6140f5a35903a38c1bb8872058b2b')

package() {
    install=gpu-trace.install
    cd "$pkgname-$pkgver"
    install -dm755 "$pkgdir/usr/bin/"
    make INSTALL_ROOT="$pkgdir" INSTALL_PREFIX="/usr/" install
    install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
    install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname/"
}
