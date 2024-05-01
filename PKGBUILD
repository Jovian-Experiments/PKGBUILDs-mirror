# Author : Clayton Craft <clayton@igalia.com>

pkgname='steamos-systemreport'
pkgver=0.7
pkgrel=2
pkgdesc='System report collection tool'
arch=('any')
license=('LGPL2.1')
url='https://gitlab.steamos.cloud/holo/holo'
source=(
  'steamos-systemreport'
  'steamos-systemreport-privileged'
  'org.valve.steamos.systemreport.policy'
)
sha256sums=(
  '3b81df0fc312929fbe1226e9f759dd9871d51af84f2cd7d51d06ef3eafd92d23'
  '45d43d374cb4adab3dfc4e144575384b5391b93914a6a6ab0f9acf26c59c1377'
  'b36473e3b77307450e75c59e248dde34d95b69c6c765a425fc30d9e201e23067'
)

package() {
  depends=(
    'bash'
    'rauc'                           # rauc status
    'drm_info'                       # drm_info
    'upower'                         # upower
    'wireplumber'                    # wpctl
    'iputils'                        # ping
    'iproute2'                       # ip
    'iwd'                            # iwctl
    'pciutils'                       # lspci
    'usbutils'                       # lsusb
    'systemd'                        # coredumpctl, journalctl
    'procps-ng'                      # ps
    'util-linux'                     # lsblk, hexdump
    'parted'                         # parted
    'smartmontools'                  # smartctl
    'steamos-customizations-jupiter' # steamos-{readonly,dump-info}
    'jupiter-hw-support'             # amd_system_info
    'polkit'
  )
  install -Dm755 steamos-systemreport -t "$pkgdir"/usr/bin/
  install -Dm755 steamos-systemreport-privileged -t "$pkgdir"/usr/bin/steamos-polkit-helpers
  install -m755 -d "$pkgdir"/usr/share/polkit-1/actions
  install -m644 org.valve.steamos.systemreport.policy -t "$pkgdir"/usr/share/polkit-1/actions
}
