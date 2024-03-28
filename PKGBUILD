# Author : Manuel A. Fernandez Montecelo <mafm@igalia.com>

pkgname='steamos-networking-tools'
pkgver=1.0
pkgrel=1
pkgdesc='SteamOS networking tools'
arch=('any')
license=('LGPL2.1')
url='https://gitlab.steamos.cloud/holo/holo'
source=("${pkgname%-git}::git+${url}#tag=${_tag}")
source=(
  'steamos-wifi-set-backend'
  'steamos-wifi-set-backend-privileged'
  'steamos-wifi-set-backend.bash-completion'
  'org.valve.steamos.wifi.set.backend.policy'
)
sha256sums=(
  '5a86f15f80474388d03000d0e51e9cf31cf9b0469ab2c9b266dc92b4af58df65'
  '75d931eaf4d4a225c52ba8af6850ff4c52490e7595edd0681d1b41d8da54de4d'
  'ebc55a73168f331d34ce03ecf0d081699faa448ae49098ecd2ce15e8081598bc'
  'd5b620c8b6cf581f1d0068611d63b17671f7383ce5ed11ab085966d9cf7574cc'
)
# depends on these at runtime, commented out as not needed at build time
# depends=(
#   'bash'
#   'iw'
#   'iwd'                            # iwd systemd unit
#   'network-manager'                # NetworkManager systemd unit and config
#   'systemd'                        # systemctl
#   'polkit'
# )

package() {
  install -Dm0755 steamos-wifi-set-backend -t "${pkgdir}"/usr/bin
  install -Dm0755 steamos-wifi-set-backend-privileged -t "${pkgdir}"/usr/bin/steamos-polkit-helpers
  install -Dm0644 steamos-wifi-set-backend.bash-completion -T "${pkgdir}"/usr/share/bash-completion/completions/steamos-wifi-set-backend
  install -m0755 -d "${pkgdir}"/usr/share/polkit-1/actions
  install -Dm0644 org.valve.steamos.wifi.set.backend.policy -t "${pkgdir}"/usr/share/polkit-1/actions
}
