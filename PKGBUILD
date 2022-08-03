# Maintainer: Vicki Pfau <vi@endrift.com>

pkgname=breakpad-hook
pkgver=0.0.1
pkgrel=1
pkgdesc="Custom hook for sending coredumps to both systemd-coredump and breakpad"
arch=('any')
license=('BSD')
depends=('python3' 'systemd' 'google-breakpad')
source=("crash-hook.py" "60-crash-hook.conf" "LICENSE")
sha256sums=('fd5e5bf2c7bac44e950666ea052b7c5c81e42d8cbbb1e63cbe3955f4603911a1'
            'c67c451920c0d2b5e5450244947a51cc5d0adf4e7401bb3ce612b61ce083f840'
            'ae5c11035ee07df58bf7f3236e0f2446cad67da53e293bb3ef743da5a422348d')

package() {
    install -Dm 755 crash-hook.py "${pkgdir}/usr/lib/crash-hook.py"
    install -Dm 644 60-crash-hook.conf "${pkgdir}/usr/lib/sysctl.d/60-crash-hook.conf"
    install -Dm 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
