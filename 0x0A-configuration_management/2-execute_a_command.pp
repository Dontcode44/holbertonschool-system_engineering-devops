# Pkill
exec {'killmenow':
command  => 'pkill',
onlyif => '/killmenow'
}
