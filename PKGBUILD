pkgname=steamos-devkit-service
pkgdesc="SteamOS Devkit Service"
pkgver=0.20250620.0
pkgrel=1
arch=('any')
url="https://gitlab.steamos.cloud/devkit/steamos-devkit-service"
license=('LGPL-2.1+')
_commit=83bfd488883a7fc6de6fb6054fc98269e6c10853
source=(
    git+https://gitlab.steamos.cloud/devkit/steamos-devkit-service.git#tag=v"$pkgver"
    steamos-devkit-service.service
    10-steamos-devkit-service-dns-sd.rules
)
sha512sums=('69653c0b35e40e9286ebfb62aca4ca007d0a38c6c8696668d308aaa36c65c59ec786b8fa4fcf4ae1bb6abc1b405bd2b424240b24441920595f6d756ae5ff50e5'
            'b028654e3a1e4a59d6ff62bf3d82bca7a6c3009507bb7b60d2abad7a37d442f0988d832b1d64bacfebc1363581bf2c78c806f9fae3f7a5c90dae9fa9d7c797e4'
            '406ae6abe9858f6a42569d1631da9c264de7a9b001ee4ff5757c80bc0ec41ffecf0ffef9987aa6bf1978827ab030f75d2c13205cefeb8e881fd470208f0215e0')
makedepends=('git' 'dbus-python' 'systemd')

package() {
    depends=('dbus-python' 'systemd')
    pkgdesc="SteamOS Devkit Service"

    cd "${pkgname}"

    mkdir -p "${pkgdir}"/usr/lib/systemd/system
    cp "${srcdir}"/steamos-devkit-service.service "${pkgdir}"/usr/lib/systemd/system/

    mkdir -p "${pkgdir}"/etc/polkit-1/rules.d
    cp "${srcdir}"/10-steamos-devkit-service-dns-sd.rules "${pkgdir}"/etc/polkit-1/rules.d/

    mkdir -p "${pkgdir}"/usr/share/steamos-devkit
    cp -r "${srcdir}"/${pkgname}/hooks "${pkgdir}"/usr/share/steamos-devkit
    cp "${srcdir}"/${pkgname}/src/steamos-devkit-service.py "${pkgdir}"/usr/share/steamos-devkit
}
